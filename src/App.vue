<template>
  <img alt="Vue logo" src="./assets/Marill.png" width="387">
  <PokemonGui msg="Pokemon Info Finder"/>
</template>

<script>
import PokemonGui from './components/PokemonGui.vue'

export default {
  name: 'App',
  components: {
    PokemonGui
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #11406e;
  margin-top: 60px;
}
</style>
