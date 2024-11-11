<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p> Search for pokemon... </p>
    <input v-model=pokemonName placeholder="Enter pokemon name here"/>
    <button @click=getPokemonDetailsByName> Search </button>
    <div v-if="gotData == true" style="align-content: center; text-align: left;"> 
        <h2> {{currentPokemonData.name[0].toUpperCase()+currentPokemonData.name.substring(1)}} </h2>
        <table>
            <thead>
                <tr>
                    <th v-for="currentPokemonStat in currentPokemonData.stats" :key="currentPokemonStat">
                      {{currentPokemonStat.stat.name.toString().padEnd(20)}}
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td v-for="currentPokemonStat in currentPokemonData.stats" :key="currentPokemonStat">
                      {{currentPokemonStat.base_stat.toString().padEnd(20)}}
                    </td>
                </tr>
                <tr>
                    <td v-for="currentPokemonStat in currentPokemonData.stats" :key="currentPokemonStat">
                      {{currentPokemonStat.effort.toString().padEnd(20)}}
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
    <div>
        <h3> Effort Value Yields: </h3>
        <form>
            <input type="checkbox" value="hpyield" id="hpyield" v-model="checkedEVs"/>
            <label for="hpyield"> HP Yield </label> <br>
            <input type="checkbox" value="attackyield" id="attackyield" v-model="checkedEVs"/>
            <label for="attackyield"> Attack Yield </label> <br>
            <input type="checkbox" value="defenseyield" id="defenseyield" v-model="checkedEVs"/>
            <label for="defenseyield"> Defense Yield </label> <br>
            <input type="checkbox"  value="spattackyield" id="spattackyield" v-model="checkedEVs"/>
            <label for="spattackyield"> Special Attack Yield </label> <br>
            <input type="checkbox"  value="spdefenseyield" id="spdefenseyield" v-model="checkedEVs"/>
            <label for="spdefenseyield"> Special Defense Yield </label> <br>
            <input type="checkbox"  value="speedyield" id="speedyield" v-model="checkedEVs"/>
            <label for="speedyield"> Speed Yield </label>
        </form>
        <button @click=getEvs> Get Checked EVs </button>
        <div v-if="gotEVData == true" style="border: 1px solid #555555; align-content: center; text-align: left;">
            <table>
                <thead>
                    <tr>
                        <th> Pokemon </th>
                        <th> HP Yield </th>
                        <th> Attack Yield </th>
                        <th> Defense Yield </th>
                        <th> Special Attack Yield </th>
                        <th> Special Defense Yield </th>
                        <th> Speed Yield </th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="currentEV in currentEVData" :key="currentEV">
                        <td>
                            {{currentEV.PokemonName[0].toUpperCase() + currentEV.PokemonName.substring(1)}}
                        </td>
                        <td>
                            {{currentEV.HPYield}}
                        </td>
                        <td>
                            {{currentEV.AttackYield}}
                        </td>
                        <td>
                            {{currentEV.DefenseYield}}
                        </td>
                        <td>
                            {{currentEV.SpAttackYield}}
                        </td>
                        <td>
                            {{currentEV.SpDefenseYield}}
                        </td>
                        <td>
                            {{currentEV.SpeedYield}}
                        </td>
                    </tr>
                </tbody> 
            </table>
        </div> 
    </div>
    
  </div>
</template>

<script>
import axios from "axios";
//import { response } from 'express';

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
    },
    getEvs(){
        var queryString="types?"
        var checkedCount = 0;
        for (const checkedEV of this.checkedEVs)
        {
            if(checkedCount > 0)
            {
                queryString+="&";
            }
            queryString+=checkedEV+"=True";
            checkedCount+=1;
        }
        const fullRequestString = this.EVS_API_PREFIX + queryString;
        axios.get(fullRequestString).then(
            response =>
            {
                this.currentEVData = response.data;
                this.gotEVData = true;
                console.log(response.data);
            }).catch(
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
      gotEVData: false,
      currentPokemonData: Object,
      currentEVData: Object,
      checkedEVs: []};
  },
  created()
  {
    this.API_PREFIX = "https://pokeapi.co/api/v2/pokemon/";
    this.EVS_API_PREFIX = "http://192.168.7.50:3080/evs/";
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
.table {
  border-collapse: collapse;
  width: 100%;
  margin-bottom: 20px;
}

th, td {
  text-align: left;
  padding: 10px 20px;
  border: 1px solid #ddd;
}

tr:nth-child(even) {
  background-color: #f2f2f2;
}
</style>
