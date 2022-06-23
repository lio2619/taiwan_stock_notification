<template>
	<div>
		<form @submit.prevent="create_user">
			<h2>
				<label for="user">姓名:&nbsp;&nbsp;&nbsp;</label>
				<input id="user" type="text" v-model.trim="user" />
			</h2>
			<h2>
				<label for="email">信箱:&nbsp;&nbsp;&nbsp;</label>
				<input id="email" type="text" v-model.trim="email" />
			</h2>
			<h2>
				<label for="stock">股票:&nbsp;&nbsp;&nbsp;</label>
				<input id="stock" type="text" v-model.trim="stock" />
			</h2>
			<h2>
				<label for="price">價錢:&nbsp;&nbsp;&nbsp;</label>
				<input id="price" type="text" v-model.trim="price" />
			</h2>
			<button v-on:click="button">提交</button>
		</form>
		<hr />
	</div>
</template>

<script>
export default {
	data() {
		return {
			user: "",
			email: "",
			stock: "",
			price: "",
		};
	},
	methods: {
		create_user() {
			alert("提交成功！！！\n");
			console.log("user", this.user);
			console.log("email", this.email);
			console.log("stock", this.stock);
			console.log("price", this.price);
		},
	},
};
</script>
