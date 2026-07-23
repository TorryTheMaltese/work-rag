export interface DocumentItem {
  id: number
  filename: string
}

export interface ChatSource {
  document_id: number
  chunk_index: number
  chunk_text: string
}

export interface ChatResponse {
  answer: string
  question: string
  sources: ChatSource[]
}

export interface ChatMessage {
  id: number
  role: 'user' | 'assistant'
  content: string
  sources?: ChatSource[]
}
