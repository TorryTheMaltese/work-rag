def split_text_into_chunks(
    text: str,
    chunk_size: int = 500,
    chunk_overlap: int = 100,
) -> list[str]:
    if chunk_size <= 0:
        raise ValueError("chunk_size는 1 이상이어야 합니다.")

    if chunk_overlap < 0:
        raise ValueError("chunk_overlap은 0 이상이어야 합니다.")

    if chunk_overlap >= chunk_size:
        raise ValueError("chunk_overlap은 chunk_size보다 작아야 합니다.")

    cleaned_text = text.strip()

    if not cleaned_text:
        return []

    chunks: list[str] = []
    start = 0
    step = chunk_size - chunk_overlap

    while start < len(cleaned_text):
        end = start + chunk_size
        chunk = cleaned_text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += step

    return chunks