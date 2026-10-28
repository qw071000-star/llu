# 고해상도 재렌더

새로 생성하지 않는다. 채택본을 원본 영상으로 붙이고, 같은 요소·같은 음성으로 다시 렌더한다.

## 필요한 정보

| 필요한 정보 | 틀의 자리 |
|---|---|
| 채택 테이크 job(OK 대장 카드), 원본 해상도, 목표 해상도 | `SOURCE VIDEO`, `RESOLUTION` |
| 원본의 샷 구성: 컷·길이·대사 | 샷 요약 |
| 원본에 붙인 요소와 순서, 음성 파일 | `ACTIVE REFERENCES` |
| 원본의 STYLE·QUALITY 문장 | `STYLE / QUALITY` |
| 확정 해상도 생성을 사용자가 지시했는가 | 생성 전 점검 |

## 틀

```text
SOURCE VIDEO: the attached video is the take to reproduce. [Shot-by-shot summary]. Every cut,
duration, line and sound stays the same.
RESOLUTION: the source is [480p/720p]; only resolution and detail differ.
ACTIVE REFERENCES: [same elements, same order, same voice files as the source].
STYLE / QUALITY: [same]. No digital sharpening.
Required: same number, order and length of shots as the source; any difference = failed take.
```
