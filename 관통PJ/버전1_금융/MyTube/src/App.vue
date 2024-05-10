<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container">
      <router-link class="navbar-brand" to="/">MyTube</router-link>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link class="nav-link" to="/">Home</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/search">Search</router-link>
          </li>
          <li class="nav-item">
            <!-- "나중에 보기" 경로 수정 -->
            <router-link class="nav-link" to="/later">Later</router-link>
          </li>
          <!-- 다른 메뉴 항목들을 여기에 추가할 수 있습니다. -->
        </ul>
      </div>
    </div>
  </nav>
  <RouterView />
</template>

<script setup>
// 필요한 import 구문 등은 여기에 추가합니다.
</script>

<style scoped>
/* 필요한 스타일이 있다면 여기에 추가합니다. */
</style>