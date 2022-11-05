<template>
  <div id="progressbar">
    <div class="container">
    <div>{{ percent }}%</div>
    <div class="loading-bar justify-content-center">
        <div class="percentage" :style="{'width': percentage + '%'}"></div>
    </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomeView',
  data () {
    return {
        percentage: 50
    }
  },
  created () {
    let interval = setInterval(() => {
      if (this.percentage < 100)
        this.percentage += .1
      else
        clearInterval(interval)
    }, 10)
  },
  computed: {
    percent() {
      return this.percentage.toFixed();
    }
  }

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
    text-align: center;
    margin:auto;
    width: 400px;
    height: 30px;
    border-radius: 15px;
    overflow: hidden;
    border-bottom: 1px solid #ddd;
    box-shadow: inset 0 1px 2px rgba($color: #000, $alpha: .4),
    0 -1px 1px #fff,  0 1px 0 #fff;
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
    background-image: linear-gradient(135deg, rgba($color:#fff, $alpha: .15) 25%, transparent 25%, transparent 50%, rgba($color: #fff, $alpha: .15) 50%,
    rgba($color: #fff, $alpha: .15) 75%, transparent 75%, transparent);
}

@keyframes animate-stripes {
    0% { background-position:0 0; }
    100% {background-position: 60px 0; }
}
</style>
