# real11-C34 소품 지적 — "왕진 가방이 너무 새 거 같아" (2턴) — PASS 2 / 부분 0 / FAIL 0 (real9: PASS 2 / 부분 0 / FAIL 0)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `image-prompt/SKILL.md`+`prop.md`만 열고 정본(대장·결정·OK 대장)을 grep으로 확인. 생성하지 않고 "아직 아무것도 생성하지 않았고". 고칠 대상을 묻는 항목 1: "`prop_doctor_bag_v1` 자산 자체를 LOCKED EDIT … (이유: 확정 job이 미기록이라 …승인된 2-1·3-1은 그대로 둠)". 사용 흔적 제안값(손잡이 손때, 모서리 닳음, 옆면 잔주름, 걸쇠 무광), Avoid 제안. 절차: "고정 설명문이 바뀌므로 새 요소 `prop_doctor_bag_v2`로 확정하고 v1은 폐기 목록으로 옮깁니다". 원인을 "worn이 모호해서 … 탓으로 보입니다"라고 쓴 것은 결과를 못 본 추정인데 "추정" 표기가 없음(경미) |
| 2 | PASS | `Edit <<<prop_doctor_bag_v1>>> WITHOUT reframing …`, CHANGE/PRESERVE(실루엣·폭 40cm·처진 옆면·스티치·걸쇠 위치)/ONLY CHANGE, `Avoid: tears, holes, heavy rust stains, brand logos, text, watermarks.`. 원본 job 미기록을 한 줄로 알림(`prop.md` 편집 규칙대로 묻지 않음), 배경은 `the existing background`, "원본의 현재 상태는 추정". 블록 밖 모드·참조·모델·1k·`fld-props`, 고정 설명문 전 → 후, 위험 5개. 대장 PR-001 아래 `초안(제안값) prop_doctor_bag_v2` 기록(diff 확인), 보내지 않음 |

## 검사기
내 실행 `--kind image --refs 1`(고정 설명문이 바뀌는 편집이라 `bag.lines` 없음): `OK — image 프롬프트 1275자, 걸린 항목 없음`

## 추가 발견
- G1 위반 없음. `tmp/` 삭제 확인. 인물 없는 프롬프트라 `LEFT and RIGHT are SCREEN directions` 없음은 정당.

## 키트 결함
없음.

## 총평
결과 지적을 생성 지시로 받지 않고, 에셋 편집·v2 절차·사용 흔적 제안값까지 모두 규칙대로 했다.
