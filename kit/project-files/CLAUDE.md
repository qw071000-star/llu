# CLAUDE.md — 「[작품명]」 AI 이미지·영상 제작 리포

@.claude/instructions.md

(위 줄은 지침 파일을 불러온다. 불러오기가 안 되는 환경이면 `.claude/instructions.md`를 먼저 읽는다.)

## 이 리포의 정본

| 무엇 | 파일 | 누가 고치나 |
|---|---|---|
| 확정 사항 | `project/decisions.md` | 총괄 세션 |
| 에셋·폴더 대장 | `project/asset-registry.md` | 총괄 세션 |
| 컷 목록·상태 | `project/shot-list.md` | 총괄 세션 |
| 컷 카드 | `project/cuts/C##.md` | 총괄이 발행. 컷 세션은 [11] 이전 시도만 고친다 |
| 핸드오프·시행착오 | `project/log/` | 누구나 추가만 한다(고치지도 지우지도 않는다) |

- 첫 메시지로 이 세션이 총괄인지 컷(C##)인지 확인한다.
- 컷 세션은 자기 컷 카드 말고 다른 컷 파일을 읽지 않는다.
- `project/log/`는 원인을 조사할 때만 읽는다.
- 파일은 해당 줄만 고친다. 정본 문서를 통째로 다시 쓰지 않는다.
- 작업별 규칙은 `.claude/skills/`에 있고, 그 작업을 할 때만 읽힌다.
