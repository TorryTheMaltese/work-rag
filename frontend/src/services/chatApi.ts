import type { ChatResponse } from '@/types'

const API_BASE_URL = 'http://localhost:8000'

export async function sendChatQuestion(question: string, limit = 3): Promise<ChatResponse> {
  const response = await fetch(`${API_BASE_URL}/chat`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      question,
      limit,
    }),
  })

  if (!response.ok) {
    const errorBody = await response.text()

    throw new Error(errorBody || `질문 전송에 실패했습니다. (${response.status})`)
  }

  return (await response.json()) as ChatResponse
}
