<script setup lang="ts">
import { ref } from 'vue'

import type { ChatMessage } from '@/types'

defineProps<{
  messages: ChatMessage[]
  isSending: boolean
}>()

const openedSourceMessageIds = ref<Set<number>>(new Set())

function toggleSources(messageId: number) {
  const next = new Set(openedSourceMessageIds.value)

  if (next.has(messageId)) {
    next.delete(messageId)
  } else {
    next.add(messageId)
  }

  openedSourceMessageIds.value = next
}

function isSourcesOpen(messageId: number): boolean {
  return openedSourceMessageIds.value.has(messageId)
}
</script>

<template>
  <section class="chat-content">
    <div v-if="messages.length === 0" class="empty-state">
      <div class="empty-icon">W</div>

      <h2>업로드한 문서를 바탕으로 질문해보세요</h2>

      <p>문서를 추가하면 관련 내용을 검색하여 답변합니다.</p>
    </div>

    <div v-else class="message-list">
      <article
        v-for="message in messages"
        :key="message.id"
        class="message-row"
        :class="`message-row--${message.role}`"
      >
        <div class="message-inner">
          <div class="message-avatar">
            {{ message.role === 'user' ? '나' : 'W' }}
          </div>

          <div class="message-body">
            <div class="message-role">
              {{ message.role === 'user' ? '사용자' : 'Work RAG' }}
            </div>

            <div class="message-content">
              {{ message.content }}
            </div>

            <div v-if="message.role === 'assistant' && message.sources?.length" class="sources">
              <button class="sources-toggle" type="button" @click="toggleSources(message.id)">
                {{
                  isSourcesOpen(message.id)
                    ? '참고 문서 닫기'
                    : `참고한 문서 내용 ${message.sources.length}개`
                }}
              </button>

              <div v-if="isSourcesOpen(message.id)" class="source-list">
                <article
                  v-for="source in message.sources"
                  :key="`${source.document_id}-${source.chunk_index}`"
                  class="source-card"
                >
                  <div class="source-title">
                    문서 {{ source.document_id }} · Chunk {{ source.chunk_index }}
                  </div>

                  <p>{{ source.chunk_text }}</p>
                </article>
              </div>
            </div>
          </div>
        </div>
      </article>

      <article v-if="isSending" class="message-row message-row--assistant">
        <div class="message-inner">
          <div class="message-avatar">W</div>

          <div class="message-body">
            <div class="message-role">Work RAG</div>
            <div class="typing-indicator">검색 중…</div>
          </div>
        </div>
      </article>
    </div>
  </section>
</template>

<style scoped>
.chat-content {
  flex: 1;
  min-height: 0;
  overflow-y: auto;
}

.empty-state {
  display: flex;
  min-height: 100%;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  padding: 40px 20px 120px;
  text-align: center;
}

.empty-icon {
  display: grid;
  width: 48px;
  height: 48px;
  margin-bottom: 20px;
  border-radius: 14px;
  background: #202123;
  color: #ffffff;
  font-size: 20px;
  font-weight: 700;
  place-items: center;
}

.empty-state h2 {
  margin: 0 0 10px;
  font-size: 24px;
}

.empty-state p {
  margin: 0;
  color: #6b7280;
}

.message-list {
  padding-bottom: 24px;
}

.message-row {
  padding: 26px 20px;
}

.message-row--assistant {
  background: #f7f7f8;
}

.message-inner {
  display: flex;
  gap: 16px;
  width: min(760px, 100%);
  margin: 0 auto;
}

.message-avatar {
  display: grid;
  flex: 0 0 auto;
  width: 34px;
  height: 34px;
  border-radius: 9px;
  background: #202123;
  color: #ffffff;
  font-size: 13px;
  font-weight: 700;
  place-items: center;
}

.message-row--user .message-avatar {
  background: #e5e7eb;
  color: #202123;
}

.message-body {
  min-width: 0;
  flex: 1;
}

.message-role {
  margin-bottom: 8px;
  font-size: 14px;
  font-weight: 700;
}

.message-content {
  line-height: 1.7;
  white-space: pre-wrap;
  overflow-wrap: anywhere;
}

.sources {
  margin-top: 18px;
}

.sources-toggle {
  padding: 8px 11px;
  border: 1px solid #d1d5db;
  border-radius: 9px;
  background: #ffffff;
  font-size: 13px;
  cursor: pointer;
}

.sources-toggle:hover {
  background: #f9fafb;
}

.source-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-top: 10px;
}

.source-card {
  padding: 14px;
  border: 1px solid #e5e7eb;
  border-radius: 10px;
  background: #ffffff;
}

.source-title {
  margin-bottom: 8px;
  color: #6b7280;
  font-size: 12px;
  font-weight: 700;
}

.source-card p {
  margin: 0;
  color: #4b5563;
  font-size: 13px;
  line-height: 1.6;
  white-space: pre-wrap;
}

.typing-indicator {
  color: #6b7280;
}

@media (max-width: 720px) {
  .message-row {
    padding-right: 14px;
    padding-left: 14px;
  }

  .message-inner {
    gap: 11px;
  }
}
</style>
