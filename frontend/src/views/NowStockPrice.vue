<template>
	<div>
		<form @submit.prevent="now_stock_price">
			<h2>
				<label for="stock">股票名稱:&nbsp;&nbsp;&nbsp;</label>
				<input id="stock" type="text" v-model.trim="stock" />
			</h2>
			<button v-on:click="button">查詢</button>
		</form>
		<hr />
	</div>
</template>

<script>
export default {
	data() {
		return {
			stock: "",
		};
	},
	methods: {
		now_stock_price() {
			console.log("stock", this.stock);
		},
	},
};
</script>
