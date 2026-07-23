import type { DocumentItem } from '@/types'

const API_BASE_URL = 'http://localhost:8000'

export async function getDocuments(): Promise<DocumentItem[]> {
  const response = await fetch(`${API_BASE_URL}/documents`)

  if (!response.ok) {
    throw new Error(`문서 목록 조회에 실패했습니다. (${response.status})`)
  }

  return (await response.json()) as DocumentItem[]
}

export async function uploadDocument(file: File): Promise<DocumentItem> {
  const formData = new FormData()
  formData.append('file', file)

  const response = await fetch(`${API_BASE_URL}/documents/upload`, {
    method: 'POST',
    body: formData,
  })

  if (!response.ok) {
    const errorBody = await response.text()

    throw new Error(errorBody || `문서 업로드에 실패했습니다. (${response.status})`)
  }

  return (await response.json()) as DocumentItem
}
