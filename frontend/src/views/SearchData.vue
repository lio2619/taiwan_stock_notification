<template>
	<div id="app">
		<form @submit.prevent="search_data">
			<h2>
				<label for="email">信箱:&nbsp;&nbsp;&nbsp;</label>
				<input id="email" type="text" v-model.trim="email" />
			</h2>
			<button v-on:click="button">查詢</button>
		</form>
		<hr />
		<h2><p>{{all_data}}</p></h2>
	</div>
</template>

<script>
import axios from 'axios';

export default {
	data() {
		return { 
			all_data: ''
		};
	},
	methods: {
		search_data(){
			axios.post('http://127.0.0.1:5000/user/get', {
				email : this.email
			})
			.then(res => {
				console.log(res.data);
				this.all_data = res.data;
			})
			.catch(error => {
				if(error.response){
					if (error.response.status == 400){
						this.all_data = '請輸入正確的信箱';
					}
				}else if(error.request){
					alert("沒有收到回應");
				}else{
					alert("伺服器請求失敗");
				}
			})
		},
	},
};
</script>
