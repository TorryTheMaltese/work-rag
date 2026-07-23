<script setup lang="ts">
import { ref } from 'vue'

defineProps<{
  isSending: boolean
  isUploading: boolean
}>()

const emit = defineEmits<{
  submit: [question: string]
  requestUpload: []
}>()

const question = ref('')

function handleKeydown(event: KeyboardEvent) {
  if (event.key !== 'Enter') {
    return
  }

  // 한글 입력 조합 중 Enter가 눌린 경우 전송 방지
  if (event.isComposing) {
    return
  }

  // Shift+Enter는 기본 줄바꿈 허용
  if (event.shiftKey) {
    return
  }

  event.preventDefault()
  submit()
}

function submit() {
  const trimmedQuestion = question.value.trim()

  if (!trimmedQuestion) {
    return
  }

  emit('submit', trimmedQuestion)
  question.value = ''
}
</script>

<template>
  <footer class="chat-composer">
    <div class="input-wrapper">
      <button
        class="attach-button"
        type="button"
        aria-label="문서 추가"
        :disabled="isUploading"
        @click="emit('requestUpload')"
      >
        ＋
      </button>

      <textarea
        v-model="question"
        rows="1"
        placeholder="문서에 대해 질문해보세요"
        :disabled="isSending"
        @keydown="handleKeydown"
      />

      <button
        class="send-button"
        type="button"
        aria-label="전송"
        :disabled="isSending || !question.trim()"
        @click="submit"
      >
        {{ isSending ? '…' : '↑' }}
      </button>
    </div>

    <p class="composer-caption">Enter로 전송 · Shift+Enter로 줄바꿈</p>
  </footer>
</template>

<style scoped>
button,
textarea {
  font: inherit;
}

button:disabled,
textarea:disabled {
  cursor: not-allowed;
  opacity: 0.55;
}

.chat-composer {
  flex: 0 0 auto;
  padding: 20px 24px 12px;
  background: linear-gradient(to top, #ffffff 72%, rgb(255 255 255 / 0%));
}

.input-wrapper {
  display: flex;
  align-items: flex-end;
  width: min(760px, 100%);
  min-height: 56px;
  padding: 8px;
  margin: 0 auto;
  border: 1px solid #d1d5db;
  border-radius: 18px;
  background: #ffffff;
  box-shadow: 0 4px 20px rgb(0 0 0 / 8%);
}

.input-wrapper:focus-within {
  border-color: #9ca3af;
}

.input-wrapper textarea {
  flex: 1;
  min-height: 40px;
  max-height: 180px;
  padding: 10px 8px;
  border: 0;
  outline: none;
  line-height: 1.45;
  resize: none;
}

.attach-button,
.send-button {
  display: grid;
  flex: 0 0 auto;
  width: 40px;
  height: 40px;
  border: 0;
  border-radius: 50%;
  cursor: pointer;
  place-items: center;
}

.attach-button {
  background: transparent;
  font-size: 21px;
}

.attach-button:hover:not(:disabled) {
  background: #f3f4f6;
}

.send-button {
  background: #202123;
  color: #ffffff;
  font-size: 20px;
}

.send-button:hover:not(:disabled) {
  background: #343541;
}

.composer-caption {
  margin: 8px 0 0;
  color: #9ca3af;
  font-size: 12px;
  text-align: center;
}

@media (max-width: 720px) {
  .chat-composer {
    padding-right: 12px;
    padding-left: 12px;
  }
}
</style>
