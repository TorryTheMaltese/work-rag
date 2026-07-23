def generate_answer(question:str, contexts:list[str]) -> str:

    # 현재 Claude API 미연결(결제X)
    # 임시로 context를 단순히 합쳐서 반환
    # Claude API 연결 후에 context를 기반으로 질문에 대한 답변을 생성하도록 구현 예정

    joined_contexts = "\n\n".join(contexts)

    return (
        "현재 Claude API는 연결되지 않았습니다.\n\n"
        f"질문: {question}\n\n"
        f"검색된 문서 내용: \n{joined_contexts}"
    )