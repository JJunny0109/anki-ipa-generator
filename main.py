from pathlib import Path
import eng_to_ipa as ipa
import pandas as pd


def convert_word_to_ipa(word: str) -> str:
    """단어를 IPA 발음기호로 변환합니다.

    eng_to_ipa는 변환 불가능한 단어 뒤에 '*'를 붙이므로, 이를 정리합니다.
    """
    if pd.isna(word) or not isinstance(word, str):
        return ""

    cleaned_word = word.strip()
    if not cleaned_word:
        return ""

    # IPA 변환 실행
    converted = ipa.convert(cleaned_word)

    # eng_to_ipa 특성상 변환할 수 없는 단어는 끝에 '*'가 붙음 (예: "apple*" -> "apple")
    if converted.endswith("*"):
        return converted.rstrip("*")

    return converted


def main():
    # 프로젝트 루트 기준 상대 경로 설정
    base_dir = Path(__file__).resolve().parent
    input_path = base_dir / "data" / "words.csv"
    output_path = base_dir / "data" / "words_with_ipa.csv"

    # 1. 입력 파일 존재 여부 확인
    if not input_path.exists():
        print(f"[Error] 입력 파일을 찾을 수 없습니다: {input_path}")
        print("data/ 폴더 안에 words.csv 파일을 넣어주세요.")
        return

    print(f"-> '{input_path.name}' 읽는 중...")
    df = pd.read_csv(input_path)

    # 2. 'Word' 열 존재 여부 확인 (대소문자 유연하게 대응)
    word_col = None
    for col in df.columns:
        if col.strip().lower() == "word":
            word_col = col
            break

    if not word_col:
        print("[Error] CSV 파일에 'Word' 열이 존재하지 않습니다.")
        print(f"현재 열 목록: {list(df.columns)}")
        return

    # 3. IPA 발음기호 변환 수행
    print("-> IPA 발음기호 변환 중...")
    df["Phonetic"] = df[word_col].apply(convert_word_to_ipa)

    # 4. 출력 디렉토리 생성 및 결과 저장
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False, encoding="utf-8-sig")

    print(f"[완료] 성공적으로 변환되었습니다! 저장 위치: {output_path}")


if __name__ == "__main__":
    main()