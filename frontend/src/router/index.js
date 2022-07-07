import { createRouter, createWebHistory } from "vue-router";

const routes = [
	{
		path: "/input_stock",
		component: () => import("../views/InputStockNamePage.vue"),
	},
	{
		path: "/search",
		component: () => import("../views/SearchData.vue"),
	},
	{
		path: "/delete",
		component: () => import("../views/DeleteData.vue"),
	},
	{
		path: "/update",
		component: () => import("../views/UpdateData.vue"),
	},
	{
		path: "/now",
		component: () => import("../views/NowStockPrice.vue"),
	},
	{
		//vue3變成catchAll(.*)才是抓取未定義的網頁 vue2是*
		path: "/:pathMatch(.*)",
		component: () => import("../views/NotFound.vue"),
	},
];

const router = createRouter({
	history: createWebHistory(process.env.BASE_URL),
	routes,
});

export default router;
