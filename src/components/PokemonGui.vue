<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p> Search for pokemon... </p>
    <input v-model=pokemonName placeholder="Enter pokemon name here"/>
    <button @click=getPokemonDetailsByName> Search </button>
    <div v-if="gotData == true" style="border: 1px solid #555555; align-content: center; text-align: left;"> 
        <h2> {{currentPokemonData.name[0].toUpperCase()+currentPokemonData.name.substring(1)}} </h2>
        <h3> Stats: </h3>
        <div v-for="currentPokemonStat in currentPokemonData.stats" :key="currentPokemonStat">
          {{currentPokemonStat.stat.name}} : {{currentPokemonStat.base_stat}} <br>
        </div>
        <h3> Effort Value Yields: </h3>
        <div v-for="currentPokemonStat in currentPokemonData.stats" :key="currentPokemonStat">
          <div v-if="currentPokemonStat.effort > 0">
            {{currentPokemonStat.stat.name}} : {{currentPokemonStat.effort}}
          </div>
        </div>
        <h3> Type </h3>
        <div v-for="currentPokemonType in currentPokemonData.types" :key="currentPokemonType">
          {{ currentPokemonType.type.name[0].toUpperCase() + currentPokemonType.type.name.substring(1) }}
        </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'PokemonGui',
  props: {
    msg: String
  },
  methods: {
    async getPokemonDetailsByName()
    {
      var apiGetString = this.API_PREFIX + this.pokemonName.toLowerCase();
      axios.get(apiGetString).then(
        response =>
        {
          console.log(response);
          this.currentPokemonData = response.data;
          this.gotData = true;
        }
      ).catch(
        function(error)
        {
          console.log(error);
        }
      )
    }
  },
  data() {
    return {
      pokemonName: "",
      gotData: false,
      currentPokemonData: Object};
  },
  created()
  {
    this.API_PREFIX = "https://pokeapi.co/api/v2/pokemon/";
    this.currentError = null;
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
