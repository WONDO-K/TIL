import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useTubeStore = defineStore('tube', () => {
  const apiKey = 'AIzaSyAcCKgSbQUuuGCzVbbD6ukAdxqo7_Mz0p4';
  const videos = ref([]);
  const laters = ref([]);

  const getVideos = function (search_query) {
    return axios.get(`https://www.googleapis.com/youtube/v3/search?key=${apiKey}&part=snippet&q=${search_query}}&maxResults=30`, {
    })
    .then((response) => {
      videos.value = response.data.items;
      console.log(response)
    })
    .catch((error) => {
      console.error(error);
    });
  };


  const addLater = function(video){
    laters.value.push(video)
  }

  const removeLater = function(videoId){
    console.log(laters)
    const idx = laters.value.findIndex(later => later.id === videoId)
    if (idx !== -1){
      laters.value.splice(idx,1)
    }
  }

  return { videos, laters, getVideos, addLater, removeLater };
}, { persist: true });
