# ComfyUI LatentSaver
### Stable Latent Save & Load for VRAM-Safe Workflows

---

## 🎥 Demo (YouTube)

▶️ YouTube Demo  
https://www.youtube.com/watch?v=YOUR_VIDEO_ID_HERE

Sampling → Latent 저장 → ComfyUI 재시작 → Load → Decode 흐름을 보여주는 데모 영상입니다.

---

## 🧠 Motivation

ComfyUI에서 영상 작업을 할 때  
Sampling 이후 Decode 단계에서 **VRAM 부족(OOM)** 으로 작업이 터지는 경우가 자주 발생합니다.

이 경우:
- Sampling부터 다시 돌려야 하고
- 이미 계산한 수백 프레임 결과가 날아가며
- 작업 흐름이 완전히 끊깁니다

**LatentSaver는 이 문제를 해결하기 위해 만들어졌습니다.**

---

## ✨ What does this node do?

### Save Latent
- Latent 값을 **output 폴더에 저장**합니다
- 저장되는 **파일 이름과 하위 경로를 직접 수정 가능**합니다
- 단, **output 폴더 내부에서만** 이름 및 경로 수정이 가능합니다

### Load Latent
- **output 폴더 안에 있는 모든 latent 파일을 자동으로 검색**
- 저장된 latent를 쉽게 찾아서 불러올 수 있습니다

---

## 🚀 Typical Use Case (VRAM OOM 대응)

1. Sampling 완료 후 **Save Latent**로 latent 저장
2. Decode 단계에서 **VRAM Out of Memory 발생**
3. ComfyUI 재시작
4. **Load Latent**로 이전 latent 불러오기
5. Decode에 바로 연결하여 이전 결과 이어서 확인

Sampling을 다시 돌릴 필요 없이  
**이전까지 만든 결과를 그대로 이어서 확인할 수 있습니다.**

---

## 🧩 How to use

### 1️⃣ Save Latent
1. Sampling 이후 latent가 출력되는 노드에 **Save Latent** 연결
2. 파일 이름 또는 경로 입력 (output 기준)
3. 실행 → latent 저장

### 2️⃣ Load Latent
1. **Load Latent** 노드 추가
2. output 폴더에 저장된 latent 파일 선택
3. 출력된 latent를 **Decode 노드에 바로 연결**

---

## 📁 File Handling Rules

- 모든 latent는 **output 폴더에만 저장**
- output 폴더 내부에서는 **하위 폴더 생성 가능**
- ComfyUI를 재시작해도 latent는 유지됩니다

---

## 📦 Installation

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/A1-multiply/ComfyUI-LatentSaver
