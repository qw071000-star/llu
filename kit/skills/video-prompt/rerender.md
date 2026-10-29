# 고해상도 재렌더

새로 생성하지 않는다. 다시 뽑으면 다른 테이크가 된다.

- **Seedance 2.5는 확인용을 `draft: true`(480p)로 보내 둔다.** 승인하면 7일 안에 `draft_job_id`로 1080p 확정본을 만든다. 같은 테이크가 그대로 올라간다. 확인용 비용은 draft가 아닌 480p와 같다.
- draft가 아니거나 기한이 지났으면 아래 틀로 채택본을 원본 영상으로 붙이고, 같은 요소·같은 음성으로 다시 렌더한다.

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

검사 `--refs`는 프롬프트의 `<<<>>>` 태그 수다. 붙이는 원본 영상은 세지 않는다.
