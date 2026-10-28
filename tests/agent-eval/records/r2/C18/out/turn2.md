맞습니다. `sim-job-3299` 0:04–0:06에 할아버지 입술이 말하려는 듯 달싹입니다. 판정은 바꾸지 않았고, 상태는 그대로 `검토`입니다.

**원인 (추정)**
- 막는 문장이 "no lip movement"까지만 막고, 입을 살짝 벌리거나 소리 없이 말하는 것(parted lips, mouthing)은 막지 않습니다.
- 0:03–0:05에 손녀가 말하는 동안 할아버지에게 맡긴 동작이 없습니다. 그런데 CHARACTER_ACTING에 "반응이 전혀 없으면 실패한 테이크"라는 줄이 있어서, 모델이 그 반응을 입으로 채운 것으로 보입니다.
- 3-2는 3-1보다 가까운 35° 화각이라 얼굴이 크게 잡힙니다. 그래서 같은 문장으로도 입이 더 쉽게 드러납니다.

**수정안 (한 가지만, AUDIO 블록에 이미 있는 문장을 바꿉니다)**
- 전: `GRANDPA does not say a single word; no attempt to speak, no lip movement.`
- 후: `GRANDPA does not say a single word: no attempt to speak, no parted lips, no mouthing.`

나머지 줄(3-1에서 가져온 ACTION_TIMING·PHYSICS 포함), 참조, 설정(Seedance 2.5 · 480p · 8초)은 그대로 둡니다. 이걸로도 다시 입이 움직이면 그다음 한 가지로, 0:03–0:05 할아버지의 망설임을 숨이나 손(엄지로 가방 걸쇠를 누름)으로 주는 방법을 쓰겠습니다.

이 결과를 거절할까요? 거절하시면 위 한 줄만 바꿔 다시 만들 수 있습니다. 생성은 "만들어"라고 하시면 보냅니다.

=== 메타 ===
연 파일(순서대로):
- RUN/.claude/skills/video-prompt/SKILL.md
- RUN/.claude/skills/video-prompt/fixes.md
- RUN/.claude/skills/acting/SKILL.md (입 움직임 검증 문장 줄만 grep)

부른 [TOOL]:
- 없음 (job 결과는 turn1의 job_display에서 확인함. 보낸 프롬프트는 이 대화에 있음)

고친 정본 파일:
- 없음 ("이상해"는 지적이므로 상태를 바꾸지 않음. 결함은 turn1에서 컷 카드 [11]에 이미 적음)
