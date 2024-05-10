<template>
  <div>
    <div class="video-search">
      <h1>비디오 검색</h1>
      <form @submit.prevent="search">
        <input type="text" v-model="search_query" placeholder="검색어를 입력하세요">
        <button type="submit">검색</button>
      </form>
    </div>
    <div class="result" v-if="tubeStore.videos.length > 0">
      <div v-for="video in tubeStore.videos" :key="video.id.channelId" class="video-item">
        <img :src="video.snippet.thumbnails.medium.url" alt="Thumbnail" @click="goDetailPage(video.id.videoId)">
        <div class="video-info">
          <b>{{ video.snippet.title }}</b>
        </div>
      </div>
    </div>
    <div v-else class="no-result">
      검색 결과가 없습니다.
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRoute,useRouter } from 'vue-router';
import { onMounted } from 'vue'
import { useTubeStore } from '@/stores/counter';

const tubeStore = useTubeStore()

const search_query = ref('')

const search = () => {
  if (search_query.value.trim() !== '') {
    tubeStore.getVideos(search_query.value);
  }
};

onMounted(() => {
  // 페이지가 로드될 때 검색어가 있으면 검색을 실행합니다.
  if (search_query.value.trim() !== '') {
    search();
  }
});

const router = useRouter()

const goDetailPage = function(videoId){
  router.push(`/${videoId}`)
}

</script>

<style scoped>
/* 비디오 검색 섹션 */
.video-search {
  margin-bottom: 20px;
}

.video-search h1 {
  margin-bottom: 10px;
  font-size: 1.5rem;
}

.video-search form {
  display: flex;
}

.video-search input {
  flex: 1;
  padding: 8px;
  font-size: 1rem;
}

.video-search button {
  padding: 8px 16px;
  font-size: 1rem;
  background-color: #007bff;
  color: #fff;
  border: none;
  cursor: pointer;
}

/* 검색 결과 섹션 */
.result {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 20px;
}

.video-item {
  border: 1px solid #ccc;
  padding: 10px;
  box-sizing: border-box;
}

.video-item img {
  width: 100%;
  height: auto;
  margin-bottom: 10px;
}

.video-info b {
  font-size: 1.2rem;
  margin-bottom: 5px;
}

.video-info p {
  font-size: 1rem;
  color: #555;
}

.no-result {
  margin-top: 20px;
  font-size: 1.2rem;
  color: #555;
}
</style>
