<template>
    <main id="app">
        <CalcView/>
    </main>
</template>

<script>
    import 'bootstrap';
    import CalcView from './components/CalcView.vue';

    export default {
        name: 'app',
        components: {
            CalcView
        }
    }
</script>

<style lang="scss">
    @import "~bootstrap/scss/bootstrap";
    html, body{min-height: 100% !important; height: 100%;}
    body{min-width: 320px;}
    #page-preloader{
        width: 100%;
        height: 100%;
        position: absolute;
        top: 0;
        right: 0;
        bottom: 0;
        left: 0;
        z-index: 10000;
        background: #FFFFFF;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    #app {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        color: #2c3e50;
        margin-top: 60px;
    }
</style>
