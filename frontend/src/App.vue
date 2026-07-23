<script setup lang="ts">
import { onMounted, ref } from 'vue'

import AppSidebar from '@/components/AppSidebar.vue'
import ChatInput from '@/components/ChatInput.vue'
import ChatWindow from '@/components/ChatWindow.vue'

import { sendChatQuestion } from '@/services/chatApi'
import { getDocuments, uploadDocument } from '@/services/documentApi'

import type { ChatMessage, DocumentItem } from '@/types'

const documents = ref<DocumentItem[]>([])
const messages = ref<ChatMessage[]>([])

const isDragging = ref(false)
const isUploading = ref(false)
const isSending = ref(false)
const isSidebarOpen = ref(false)

const fileInput = ref<HTMLInputElement | null>(null)

let nextMessageId = 1

onMounted(() => {
  void loadDocuments()
})

async function loadDocuments() {
  try {
    documents.value = await getDocuments()
  } catch (error) {
    console.error('문서 목록 조회 오류:', error)
  }
}

function isPdfFile(file: File): boolean {
  return file.type === 'application/pdf' || file.name.toLowerCase().endsWith('.pdf')
}

function openFilePicker() {
  if (isUploading.value) {
    return
  }

  fileInput.value?.click()
}

function handleFileSelect(event: Event) {
  const input = event.target as HTMLInputElement
  const file = input.files?.[0]

  if (file) {
    void handleUpload(file)
  }

  // 같은 파일을 다시 골라도 change 이벤트가 발생하도록 초기화
  input.value = ''
}

async function handleUpload(file: File) {
  if (!isPdfFile(file)) {
    window.alert('PDF 파일만 업로드할 수 있습니다.')
    return
  }

  isUploading.value = true

  try {
    await uploadDocument(file)

    // DB의 실제 문서 목록을 다시 조회
    await loadDocuments()
  } catch (error) {
    console.error('문서 업로드 오류:', error)

    window.alert(error instanceof Error ? error.message : '문서를 업로드하지 못했습니다.')
  } finally {
    isUploading.value = false
  }
}

function handleDragEnter() {
  isDragging.value = true
}

function handleDragOver() {
  isDragging.value = true
}

function handleDragLeave(event: DragEvent) {
  const currentTarget = event.currentTarget as HTMLElement | null
  const relatedTarget = event.relatedTarget as Node | null

  if (currentTarget && relatedTarget && currentTarget.contains(relatedTarget)) {
    return
  }

  isDragging.value = false
}

function handleDrop(event: DragEvent) {
  isDragging.value = false

  const file = event.dataTransfer?.files[0]

  if (file) {
    void handleUpload(file)
  }
}

async function handleSubmitQuestion(question: string) {
  messages.value.push({
    id: nextMessageId++,
    role: 'user',
    content: question,
  })

  isSending.value = true

  try {
    const response = await sendChatQuestion(question)

    messages.value.push({
      id: nextMessageId++,
      role: 'assistant',
      content: response.answer,
      sources: response.sources,
    })
  } catch (error) {
    console.error('질문 전송 오류:', error)

    messages.value.push({
      id: nextMessageId++,
      role: 'assistant',
      content:
        error instanceof Error
          ? `오류가 발생했습니다.\n${error.message}`
          : '질문 처리 중 오류가 발생했습니다.',
    })
  } finally {
    isSending.value = false
  }
}

function toggleSidebar() {
  isSidebarOpen.value = !isSidebarOpen.value
}

function closeSidebar() {
  isSidebarOpen.value = false
}
</script>

<template>
  <div
    class="app-shell"
    @dragenter.prevent="handleDragEnter"
    @dragover.prevent="handleDragOver"
    @dragleave="handleDragLeave"
    @drop.prevent="handleDrop"
  >
    <input
      ref="fileInput"
      class="file-input"
      type="file"
      accept="application/pdf,.pdf"
      @change="handleFileSelect"
    />

    <div v-if="isSidebarOpen" class="sidebar-backdrop" @click="closeSidebar" />

    <AppSidebar
      :documents="documents"
      :is-uploading="isUploading"
      :is-open="isSidebarOpen"
      @request-upload="openFilePicker"
      @close="closeSidebar"
    />

    <main class="chat-page">
      <header class="chat-header">
        <button class="menu-button" type="button" aria-label="사이드바 열기" @click="toggleSidebar">
          ☰
        </button>

        <h1>새 대화</h1>
      </header>

      <ChatWindow :messages="messages" :is-sending="isSending" />

      <ChatInput
        :is-sending="isSending"
        :is-uploading="isUploading"
        @submit="handleSubmitQuestion"
        @request-upload="openFilePicker"
      />
    </main>

    <div v-if="isDragging" class="drop-overlay">
      <div class="drop-card">
        <strong>PDF를 여기에 놓아주세요</strong>

        <span> 문서를 업로드하고 검색에 사용할 수 있습니다. </span>
      </div>
    </div>

    <div v-if="isUploading" class="upload-status">문서를 분석하고 있습니다…</div>
  </div>
</template>

<style>
* {
  box-sizing: border-box;
}

html,
body,
#app {
  width: 100%;
  min-width: 320px;
  min-height: 100%;
  margin: 0;
}

body {
  font-family:
    Pretendard,
    Inter,
    -apple-system,
    BlinkMacSystemFont,
    'Segoe UI',
    sans-serif;
  color: #202123;
}

.app-shell {
  display: flex;
  min-width: 320px;
  min-height: 100vh;
  overflow: hidden;
  background: #ffffff;
}

.file-input {
  display: none;
}

.chat-page {
  display: flex;
  flex: 1;
  flex-direction: column;
  min-width: 0;
  height: 100vh;
}

.chat-header {
  display: flex;
  flex: 0 0 60px;
  align-items: center;
  gap: 10px;
  height: 60px;
  padding: 0 24px;
  border-bottom: 1px solid #eeeeee;
}

.chat-header h1 {
  margin: 0;
  font-size: 16px;
}

.menu-button {
  display: none;
  width: 38px;
  height: 38px;
  border: 0;
  border-radius: 8px;
  background: transparent;
  font-size: 21px;
  cursor: pointer;
}

.menu-button:hover {
  background: #f3f4f6;
}

.drop-overlay {
  position: fixed;
  z-index: 100;
  display: grid;
  background: rgb(17 24 39 / 45%);
  inset: 0;
  place-items: center;
  pointer-events: none;
}

.drop-card {
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding: 34px 48px;
  border: 2px dashed #ffffff;
  border-radius: 18px;
  background: rgb(255 255 255 / 96%);
  text-align: center;
  box-shadow: 0 20px 60px rgb(0 0 0 / 20%);
}

.drop-card strong {
  font-size: 20px;
}

.drop-card span {
  color: #6b7280;
}

.upload-status {
  position: fixed;
  right: 24px;
  bottom: 24px;
  z-index: 110;
  padding: 12px 16px;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  background: #ffffff;
  box-shadow: 0 8px 30px rgb(0 0 0 / 15%);
  font-size: 14px;
}

.sidebar-backdrop {
  display: none;
}

@media (max-width: 720px) {
  .menu-button {
    display: grid;
    place-items: center;
  }

  .sidebar-backdrop {
    position: fixed;
    z-index: 20;
    display: block;
    background: rgb(17 24 39 / 38%);
    inset: 0;
  }

  .chat-header {
    padding: 0 14px;
  }

  .drop-card {
    width: calc(100% - 32px);
    padding: 28px 20px;
  }
}
</style>
