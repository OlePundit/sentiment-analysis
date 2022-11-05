<template>
  <div id="progressbar">
    <div class="container">
    <div></div>
    <div class="loading-bar">
        <div class="percentage" :style="{'width': percentage + '%'}"></div>
    </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Progressbar',
  data () {
    return {
        percentage: 0
    }
  },
  created () {

  }

</script>

<style scoped lang="scss">
#app {
    color: #222;
    width: 100%;
    height:100vh;
    background: linear-gradient(to bottom, #efefef, #ccc);
}
.loading-bar {
    position: relative;
    width: 400px;
    height: 30px;
    border-radius: 15px;
    overflow: hidden;
    border-bottom: 1px solid #ddd;
    box-shadow: inset 0 1px 2px rgba($color: #000, $alpha: .4),
    0 -1px 1px #fff,  0 1pc 0 #fff;
}
.percentage {
    position: absolute;
    top: 1px; left: 1px; right: 1px;
    display: block;
    height:100%;
    border-radius:15px;
    background-color: #a5df41;
    background-size: 30px 30px;
    animation: animate-stripes;
}

@key-frames animate-stripes {
    0% { background-position:0 0; }
    100% {background-position: 60px 0; }
}
</style>