<script setup>
import { ref } from 'vue'

const dt = ref(Date())
const setDt = () => {
  dt.value = Date()
  setTimeout(setDt, 1000)
}
setDt()

const names_input = ref('')
const names = ref([])
const presenter = ref('')
const qna = ref([])
const show_res = ref(0)

const shuffle = (arr) => {
  // https://cpro95.tistory.com/504
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1))
    const tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
  }
}

const process = () => {
  // 오늘의 발표자 한 명 뽑기
  presenter.value = names.value[Math.floor(Math.random() * names.value.length)]

  // 질문 -> 답변
  const tmp_arr = [...names.value]
  while (true) {
    // 멤버 목록 섞고
    shuffle(tmp_arr)

    // 질문 === 답변 있는지 확인
    let isSame = false
    for (let i = 0; i < tmp_arr.length; i++) {
      isSame |= names.value[i] === tmp_arr[i]
    }

    // 질문 == 답변 없다면 끝, 있다면 다시 섞기
    if (!isSame) break
  }
  qna.value = names.value.map((e, i) => [e, tmp_arr[i]])

  show_res.value = 2
}

const draw = () => {
  if (!names_input.value) {
    alert('이름을 입력해주세요!')
    return
  }

  names.value = Array.from(names_input.value.matchAll(/[가-힣]+/g)).map((e) => e[0])
  if (names.value.length == 0) {
    alert('형식에 맞춰 입력해주세요!')
    return
  }

  show_res.value = 1
  setTimeout(process, 3000)
}
</script>

<template>
  <div class="container max-w-lg mx-auto my-6 flex flex-col gap-6">
    <h1 class="text-center text-3xl border rounded p-6">! 스터디 발표자, 질문 순서 뽑기 !</h1>
    <div>
      <h2 class="text-xl">스터디 일시:</h2>
      <div class="text-center">
        <span>{{ dt }}</span>
      </div>
    </div>

    <label class="form-control">
      <h2 class="text-xl">참여 인원</h2>
      <div class="label"></div>
      <input
        id="people"
        type="text"
        v-model="names_input"
        @keyup.enter="draw"
        placeholder="김철수, 김영희, 홍길동"
        class="input input-bordered w-full"
      />
    </label>

    <div class="text-center">
      <button class="btn btn-outline btn-accent btn-wide" @click="draw">Go!</button>
    </div>

    <Transition>
      <div v-show="show_res == 1" class="p-2 text-center">
        <span class="loading loading-spinner loading-lg"></span>
      </div>
    </Transition>

    <Transition>
      <div v-show="show_res == 2">
        <div class="text-center border rounded my-6 p-2">
          <h2 class="text-xl">오늘의 발표자</h2>
          <p class="text-2xl">{{ presenter }}</p>
        </div>

        <div class="text-center border rounded my-6 p-2">
          <table class="table table-zebra text-center">
            <thead>
              <tr>
                <th><span class="text-lg">질문</span></th>
                <th><span class="text-lg">→</span></th>
                <th><span class="text-lg">답변</span></th>
              </tr>
            </thead>
            <tbody>
              <tr class="hover" v-for="(item, index) in qna" :key="index">
                <td>{{ item[0] }}</td>
                <td>→</td>
                <td>{{ item[1] }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </Transition>
  </div>
</template>

<style scoped>
/* https://vuejs.org/guide/built-ins/transition */
.v-enter-active,
.v-leave-active {
  transition: opacity 0.5s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}
</style>
