<template>
  <div v-if="video.snippet" class="video-details">
    <h2>{{ video.snippet.title }}</h2>
    <p>업로드 날짜: {{ formatDate(video.snippet.publishedAt) }}</p>
    <iframe width="560" height="315" :src="embedVideo(video.id)" frameborder="0" allowfullscreen></iframe>
    <p>{{ video.snippet.description }}</p>
    <div>
      <button v-if="!isSaved(video.id)" @click="tubeStore.addLater(video)">나중에 볼 영상 저장</button>
      <button v-else @click="tubeStore.removeLater(video.id)">저장 해제</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { useTubeStore } from '@/stores/counter'

const tubeStore = useTubeStore()
const route = useRoute()
const videoId = route.params.videoId;
const video = ref({});
const apiKey = 'AIzaSyAcCKgSbQUuuGCzVbbD6ukAdxqo7_Mz0p4';

// videoId를 기반으로 동영상의 상세 정보를 가져오는 함수
const getVideoDetail = function () {
  console.log(videoId)
  return axios.get(`https://www.googleapis.com/youtube/v3/videos?id=${videoId}&key=${apiKey}&part=snippet`)
    .then((response) => {
      video.value = response.data.items[0];
      console.log(response.data.items[0])
    })
    .catch((error) => {
      console.error(error);
    });
};

// 페이지가 로드될 때 상세 정보를 가져옴.
onMounted(() => {
  getVideoDetail();
});

// 업로드 날짜를 형식화하는 함수
const formatDate = (dateString) => {
  const date = new Date(dateString);
  return `${date.getFullYear()}년 ${date.getMonth() + 1}월 ${date.getDate()}일`;
};

// YouTube 동영상을 임베드하는 URL을 생성하는 함수
const embedVideo = (videoId) => {
  return `https://www.youtube.com/embed/${videoId}`;
};

const isSaved = function (videoIdvideoId) {
  const laters = tubeStore.laters;
  return laters.some(video => video.id === videoId);
}
</script>

<style scoped>
.video-details {
  border: 1px solid #ccc; /* 테두리 스타일 추가 */
  padding: 20px; /* 내부 여백 추가 */
  margin-top: 20px; /* 위쪽 여백 추가 */
}
</style>
