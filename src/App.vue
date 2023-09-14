<template>
  <center>
    <img alt="Vue logo" src="./assets/logo.png" style="max-width: 300px; min-width:100px;" ref="logo">
    <h1>
      <em><strong>Recommended AI Tools</strong></em>
    </h1>
  </center>
  
  <ItemCard/>
</template>

<script>
import ItemCard from './components/item-card.vue'

export default {
  name: 'App',
  components: {
    ItemCard
  }
  
}
</script>

<style scoped>
@import url(https://fonts.googleapis.com/css?family=Pinyon+Script);
@import url(https://fonts.googleapis.com/css?family=Raleway:400,700);
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
h1 {
  text-transform: uppercase;
  letter-spacing: .1em;
  
  &>em, &>strong {
    font-size: 0;
    text-align: center;
    padding: 0 1em;
    position: relative;
    display: block;

    &:before, &:after { 
      font-size: 0.5rem;
      content: '';
      display: inline-block;
      vertical-align: middle;
      width: 15%;
      max-width: 7em;
      height: 3px;
      background: #000;
      border-radius: 50%;
      position: relative;
      top: -.3em; 
    }
    
    &>strong, &>em {
      font: normal 3.5rem/1 "Pinyon Script", serif;
      font-style: normal;
      text-transform: none;
      letter-spacing: 0;
      max-width: 70%;
      display: inline-block;
      vertical-align: middle;
      padding: 0 .2em 0;
    }
    @media (min-width: 300px) {
      &>strong, &>em {
        font: normal 2.5rem/1 "Pinyon Script", serif;
      }
    }
  }
  
}
</style>
