# 퍼스트 프레임 (영상의 시작 이미지)

## 규칙

- **그 컷 영상의 0:00 상태를 만든다.** 썸네일 순간이 아니다.
- **장소 뷰, 인물 시트, 소품 요소를 권한 블록으로 묶는다.** CAMERA 블록이 모든 참조를 이긴다.
- **인물은 기존 앵커에 둔다.**
  - 위치는 거리와 접촉으로 쓴다. "근처에"는 지켜지지 않는다.
  - 동작 도중의 상태로 쓴다.
- **의상 문장은 에셋 대장 문장을 글자 그대로 쓴다.** 인물 시트의 배경·조명·포즈는 `DO NOT TRANSFER`에 적는다.
- **콘티 썸네일은 참조로 붙이지 않는다.** 그 구도가 필요하면 같은 구도의 빈 장소 이미지를 먼저 만들어 장소 참조로 쓴다.
- **소품 크기는 cm와 신체 기준으로 적는다.**
- **이웃 컷과 비교한다.** 시점과 구도가 겹치지 않는지, 빛 방향이 같은지 본다.

## 틀

```text
FIRST FRAME of a film shot — the exact state at 0:00 of the video. LEFT and RIGHT are SCREEN directions.
Using <<<LOC>>> as the exact same location, generate a new view. [CAMERA: position by objects, height,
direction, distance, shot size + camera body/lens/film stock.]
REFERENCE AUTHORITY:
- <<<LOC>>>: geography, materials, landmarks, light direction
- <<<CHAR>>>: face, hair, wardrobe only — Same face, same bone structure, same hair, same wardrobe.
  Change only the pose, framing, location and lighting.
- <<<PROP>>>: shape, material and state only; size as described below
DO NOT TRANSFER: the character sheet's backdrop, studio lighting, pose or framing.
PRIORITY: the CAMERA block overrides every reference.
BLOCKING: [each person at an existing anchor: distance and contact, mid-[action]].
WARDROBE: [asset registry sentence, verbatim].
PROP: [position, state, who holds it, size in cm and body terms].
[Nothing else / palette / material truth / light logic / era lock]
```
