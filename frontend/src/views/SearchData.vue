<template>
	<div>
		<form @submit.prevent="search_data">
			<h2>
				<label for="email">信箱:&nbsp;&nbsp;&nbsp;</label>
				<input id="email" type="text" v-model.trim="email" />
			</h2>
			<button v-on:click="button">更新</button>
		</form>
		<hr />
	</div>
</template>

<script>
export default {
	data() {
		return {
			email: "",
		};
	},
	methods: {
		search_data() {
			console.log("email", this.email);
		},
	},
};
</script>
