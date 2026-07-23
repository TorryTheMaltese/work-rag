<script setup lang="ts">
import type { DocumentItem } from '@/types'

defineProps<{
  documents: DocumentItem[]
  isUploading: boolean
  isOpen: boolean
}>()

const emit = defineEmits<{
  requestUpload: []
  close: []
}>()
</script>

<template>
  <aside class="sidebar" :class="{ 'sidebar--open': isOpen }">
    <div class="sidebar-header">
      <div class="brand">Work RAG</div>

      <button
        class="sidebar-close-button"
        type="button"
        aria-label="사이드바 닫기"
        @click="emit('close')"
      >
        ×
      </button>
    </div>

    <button
      class="upload-button"
      type="button"
      :disabled="isUploading"
      @click="emit('requestUpload')"
    >
      <span aria-hidden="true">＋</span>
      {{ isUploading ? '문서 처리 중...' : '문서 추가' }}
    </button>

    <section class="document-section">
      <h2>업로드한 문서</h2>

      <p v-if="documents.length === 0" class="document-empty">아직 업로드한 문서가 없습니다.</p>

      <ul v-else class="document-list">
        <li v-for="document in documents" :key="document.id" :title="document.filename">
          <span class="document-icon" aria-hidden="true"> ▤ </span>

          <span class="document-name">
            {{ document.filename }}
          </span>
        </li>
      </ul>
    </section>
  </aside>
</template>

<style scoped>
button {
  font: inherit;
}

button:disabled {
  cursor: not-allowed;
  opacity: 0.55;
}

.sidebar {
  z-index: 30;
  display: flex;
  flex: 0 0 280px;
  flex-direction: column;
  width: 280px;
  min-height: 100vh;
  padding: 18px 14px;
  border-right: 1px solid #e5e7eb;
  background: #f7f7f8;
}

.sidebar-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.brand {
  padding: 8px 10px 20px;
  font-size: 20px;
  font-weight: 700;
}

.sidebar-close-button {
  display: none;
  width: 36px;
  height: 36px;
  border: 0;
  border-radius: 8px;
  background: transparent;
  font-size: 24px;
  cursor: pointer;
}

.sidebar-close-button:hover {
  background: #ececf1;
}

.upload-button {
  display: flex;
  gap: 8px;
  align-items: center;
  width: 100%;
  padding: 12px 14px;
  border: 1px solid #d1d5db;
  border-radius: 10px;
  background: #ffffff;
  cursor: pointer;
}

.upload-button:hover:not(:disabled) {
  background: #f9fafb;
}

.document-section {
  min-height: 0;
  margin-top: 28px;
}

.document-section h2 {
  padding: 0 10px;
  margin: 0 0 8px;
  color: #6b7280;
  font-size: 13px;
}

.document-empty {
  padding: 10px;
  color: #9ca3af;
  font-size: 13px;
}

.document-list {
  max-height: calc(100vh - 180px);
  padding: 0;
  margin: 0;
  overflow-y: auto;
  list-style: none;
}

.document-list li {
  display: flex;
  gap: 9px;
  align-items: center;
  min-width: 0;
  padding: 10px;
  border-radius: 8px;
  cursor: pointer;
}

.document-list li:hover {
  background: #ececf1;
}

.document-icon {
  flex: 0 0 auto;
  color: #6b7280;
}

.document-name {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

@media (max-width: 720px) {
  .sidebar {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    width: min(86vw, 300px);
    transform: translateX(-100%);
    transition: transform 180ms ease;
    box-shadow: 12px 0 40px rgb(0 0 0 / 12%);
  }

  .sidebar--open {
    transform: translateX(0);
  }

  .sidebar-close-button {
    display: grid;
    place-items: center;
  }
}
</style>
