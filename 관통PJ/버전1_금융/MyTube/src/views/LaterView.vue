<template>
  <div>
    <h1>나중에 볼 영상</h1>
    <div v-if="tubeStore.laters.length > 0" class="video-list">
      <div v-for="later in tubeStore.laters" :key="later.id" class="video-item">
        <!-- 이미지와 제목을 좌우로 나란히 배치 -->
        <div class="video-content">
          <img :src="later.snippet.thumbnails.medium.url" alt="Thumbnail" @click="goDetailPage(later.id)">
          <b>{{ later.snippet.title }}</b>
        </div>
      </div>
    </div>
    <div v-else>
      저장된 동영상이 없습니다.
    </div>
  </div>
</template>

<script setup>
import { useTubeStore } from '@/stores/counter'; 
import { useRouter } from 'vue-router';

const tubeStore = useTubeStore()
const router = useRouter()

const goDetailPage = function(videoId){
  console.log(videoId)
  router.push(`/${videoId}`)
}
</script>

<style scoped>
/* 비디오 리스트의 간격을 조정 */
.video-list {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

/* 각 비디오 아이템의 스타일 */
.video-item {
  width: calc(33.33% - 20px); /* 3개의 열로 배치, 간격 제외 */
}

/* 비디오의 이미지와 제목을 가로로 나란히 배치하는 스타일 */
.video-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

/* 이미지 스타일 */
.video-content img {
  width: 100%;
  height: auto;
}

/* 제목 스타일 */
.video-content b {
  margin-top: 10px; /* 이미지와의 간격 조정 */
}
</style>
