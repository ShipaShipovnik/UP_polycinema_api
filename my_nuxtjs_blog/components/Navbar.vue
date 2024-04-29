<template>
    <nav class="navbar yellow-bg navbar-expand-sm ">
        <div class="container-fluid">
            <a href="/" class="navbar-brand">
                <img src="https://github.com/ShipaShipovnik/polycinema_site/blob/main/src/img/logo2.png?raw=true"
                    alt="logo" class="logo">
            </a>
            <div class="navbar-collapse navbar" id="mynavbar">
                <ul class="navbar-nav me-auto">
                    <li class="nav-item">
                        <nuxt-link class="link-black px-2" to="/">Главная</nuxt-link>
                    </li>
                    <li class="nav-item">
                        <nuxt-link class="link-black px-2" to="/contact">Контакты</nuxt-link>
                    </li>
                </ul>
                <form class="d-flex col-md-3">
                    <input name="q" v-model="q" type="text" class="form-control me-2 form-control-dark"
                        placeholder="Поиск" aria-label="Поиск">
                    <button class="btn btn-dark ml-2" type="submit" @click.stop.prevent="submit()">Поиск</button>
                </form>
                <div class="">
                    <span class="navbar-text mr-2" v-if="user">{{ user.username }}</span>
                    <span v-if="loggedIn"><nuxt-link class="btn btn-outline-light mr-2"
                            to="/signout">Выход</nuxt-link></span>
                    <span v-else>
                        <nuxt-link class="btn btn-outline-dark me-2" to="/signin">Вход</nuxt-link>
                        <nuxt-link class="btn btn-dark" to="/signup">Регистрация</nuxt-link>
                    </span>
                </div>
            </div>
        </div>
    </nav>
</template>

<script>
export default {
    data() {
        return {
            q: null,
        }
    },
    methods: {
        submit() {
            this.$router.push("/search?q=" + this.q);
        }
    },
    computed: {
        loggedIn() {
            return this.$auth.loggedIn
        },
        user() {
            return this.$auth.user
        }
    }
}
</script>

<style scoped></style>