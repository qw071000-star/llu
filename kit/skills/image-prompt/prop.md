# 소품

## 필요한 정보

| 필요한 정보 | 틀의 자리 |
|---|---|
| 물건, 재질, 사용 흔적 | `[prop]`, `[Use marks]` |
| 크기(cm + 신체 기준) | 크기 단서, 에셋 대장 |
| 무게로 본 물성 | 에셋 대장 (영상의 `PHYSICS`) |
| 나오면 안 되는 재질·형태 | `Avoid` |
| 이야기 속 상태 변화, 누가 어느 손(화면 쪽 + 물건)에 드는가 | 에셋 대장 상태 머신 |
| 고치기면: 어느 결과를 말하는가(그 컷의 job / 에셋 자체) | 고칠 대상 |

## 규칙

- **상태·손·크기가 바뀌는 소품은 독립 에셋으로 만든다.** 사용감을 준다.
- **크기는 장면에서 정한다.** 스튜디오 소품을 참조로 쓰면 크기가 틀어진다. 영상용 요소는 장면 프레임에서 잘라 만든다.
- **고정 설명문은 재질·모양·크기·사용 흔적만 쓴다.** 상태(열림·닫힘), 자세(처짐·들림), 손은 넣지 않는다. 그것들은 상태 머신과 컷 프롬프트에 쓴다.
- **물성은 무게로 쓴다.** 처짐, 부풀지 않음, 각이 서지 않음처럼 쓴다.
- **상태는 상태 머신으로 관리한다.** 컷 사이의 상태는 `shot-list.md` 연속성 표에 둔다.
- **확정 소품 고치기:** 에셋 이미지를 LOCKED EDIT(`SKILL.md` §3)로 고치고 크기·모양은 PRESERVE에 둔다. 고정 설명문이 바뀌면 새 요소 ID(`prop_<물건>_v2`)로 확정하고 옛 것은 에셋 대장 폐기 목록으로 옮긴다.
  - 옛 요소로 승인된 컷은 그대로 둔다. 다시 만들지는 컷마다 묻는다.

## 틀

```text
Photorealistic product-reference photograph of [prop: material, wear, size cue], isolated on a plain
seamless light grey studio background, nothing else in frame — no scene, no room, no other objects,
no hands, no people. [Use marks.] Soft even studio lighting from the front-top, minimal shadow.
Sharp focus throughout. Avoid: [wrong materials], brand logos, text, watermarks.
```
