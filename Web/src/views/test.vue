<template>
  <div>
    <div class="container mt-10">
      <div class="card bg-white">
        <img style="" :src="image" alt="" />
        <input
          @change="handleImage"
          class="custom-input"
          type="file"
          accept="image/*"
        />
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style>
* {
  font-family: Arial, Helvetica, sans-serif;
}

body {
  background: #d8dddb;
}

.container {
  display: flex;
  justify-content: center;
}

.mt-10 {
  margin-top: 10rem;
}

.bg-white {
  background: #fff;
}

.card {
  height: 10rem;
}
</style>
