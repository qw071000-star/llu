# real11-C24 실사 영상, 연기를 새로 — 3-2 (2턴) — PASS 2 / 부분 0 / FAIL 0 (real9: PASS 1 / 부분 1 / FAIL 0; real10-recheck: PASS)

| 턴 | 판정 | 근거 |
|---|---|---|
| 1 | PASS | `video-prompt` SKILL + `live-action.md`만(`acting`·`ok-reuse.md` 안 엶, 1턴 읽기 목록에 없음). 카드 [1]의 "3-1과 같은 동작·타이밍"과 "연기는 새로"가 어긋난다고 짚고(이 컷만 적용), 대사·손녀/할아버지 연기(목표·손·시선·범위 양 끝)·끝 프레임(3-3 첫 프레임을 위해 발 고정)을 제안값+이유로 5개. 렌즈 알림 35°↔75mm(32°). 카드 파일을 만들지 않음 |
| 2 | PASS | 이 턴에 `acting` SKILL을 엶(bash `cat`, 그리고 정정 문장 포함). `CHARACTER_ACTING`: 인물마다 상대를 향한 목표, 손의 일, 몸·호흡, 눈, 양 끝 failed take(`trembling voice = failed take`, `bright cheerful tone = failed take` / `a sigh, a frown … = failed take`, `a face that shows nothing at all = failed take`). 비트는 시선·사이, 사건 3개(회전·대사·손 쥐기). 목소리 문장은 대장과 글자 그대로, 할아버지 입 잠금 있음, 절제 레지스터 안. 3-1 OK 문장 안 가져옴. WARN 6,312자: 이유(인물 2·참조 4, 줄이려면 고정 문장·감정 양 끝을 지워야 함)와 숫자를 적었음 |

검사기: `--kind video C24_t2 --refs 4 --seconds 8 --must-include grandpa+girl+bag+light` → `WARN 길이 6312자. 5,500자 이하가 안전했다 — FAIL 0 · WARN 1` (플레이어가 이유와 숫자를 적었으므로 허용; 다만 "약 550자가 더 남습니다"는 실제 초과 812자와 다름)
추가 발견: 카드 [1]·[4]~[6]을 `(제안값)`으로 고침(diff). `PRE_SHOT_CONTINUITY`를 맨 앞에 둠 — `live-action.md:8` "이어받은 상태가 있을 때만"에 부합.
키트 결함: 없음.
총평: real10 수정이 유지됨.
