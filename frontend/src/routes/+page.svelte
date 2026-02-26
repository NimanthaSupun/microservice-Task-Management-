<script>
	import { onMount } from 'svelte';

	/** @type {any[]} */
	let tasks = [];
	let newTask = { title: '', description: '' };
	let loading = true;
	/** @type {string | null} */
	let error = null;

	// Use the Kong Gateway URL
	const API_URL = 'http://localhost:8000/api/tasks';

	async function fetchTasks() {
		try {
			const res = await fetch(API_URL);
			if (!res.ok) throw new Error('Failed to fetch tasks');
			tasks = await res.json();
		} catch (/** @type {any} */ e) {
			error = e.message;
		} finally {
			loading = false;
		}
	}

	async function createTask() {
		try {
			const res = await fetch(API_URL, {
				method: 'POST',
				headers: { 'Content-Type': 'application/json' },
				body: JSON.stringify(newTask)
			});
			if (!res.ok) throw new Error('Failed to create task');
			
			// Reset form and refresh list
			newTask = { title: '', description: '' };
			await fetchTasks();
			alert('Task Created & Notification Queued!');
		} catch (/** @type {any} */ e) {
			alert('Error: ' + e.message);
		}
	}

	onMount(fetchTasks);
</script>

<main class="container">
	<header>
		<h1>🚀 Task Manager Pro</h1>
		<p class="subtitle">Powered by Microservices & Kong Gateway</p>
	</header>

	<section class="form-card">
		<h2>Create New Task</h2>
		<div class="input-group">
			<input type="text" bind:value={newTask.title} placeholder="Task Title" />
			<textarea bind:value={newTask.description} placeholder="Task Description"></textarea>
			<button on:click={createTask}>Add Task</button>
		</div>
	</section>

	<section class="task-list">
		<h2>Your Tasks</h2>
		
		{#if loading}
			<p>Loading tasks...</p>
		{:else if error}
			<p class="error">{error}</p>
		{:else if tasks.length === 0}
			<p>No tasks found. Create your first one above!</p>
		{:else}
			<div class="grid">
				{#each tasks as task}
					<div class="card">
						<h3>{task.title}</h3>
						<p>{task.description}</p>
						<span class="badge {task.status}">{task.status}</span>
					</div>
				{/each}
			</div>
		{/if}
	</section>
</main>

<style>
	:global(body) {
		background-color: #0f172a;
		color: #f8fafc;
		font-family: 'Inter', system-ui, sans-serif;
		margin: 0;
		padding: 0;
	}

	.container {
		max-width: 800px;
		margin: 0 auto;
		padding: 2rem;
	}

	header {
		text-align: center;
		margin-bottom: 3rem;
	}

	h1 {
		font-size: 3rem;
		margin: 0;
		background: linear-gradient(to right, #38bdf8, #818cf8);
		background-clip: text;
		-webkit-background-clip: text;
		-webkit-text-fill-color: transparent;
	}
/* ... rest of the CSS stays the same ... */

	.subtitle {
		color: #94a3b8;
		font-size: 1.1rem;
	}

	.form-card {
		background: #1e293b;
		padding: 2rem;
		border-radius: 1rem;
		box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
		margin-bottom: 3rem;
	}

	.input-group {
		display: flex;
		flex-direction: column;
		gap: 1rem;
	}

	input, textarea {
		background: #334155;
		border: 1px solid #475569;
		padding: 0.8rem;
		border-radius: 0.5rem;
		color: white;
		font-size: 1rem;
	}

	button {
		background: #3b82f6;
		color: white;
		border: none;
		padding: 1rem;
		border-radius: 0.5rem;
		font-weight: bold;
		cursor: pointer;
		transition: background 0.2s;
	}

	button:hover {
		background: #2563eb;
	}

	.grid {
		display: grid;
		grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
		gap: 1.5rem;
	}

	.card {
		background: #1e293b;
		padding: 1.5rem;
		border-radius: 0.8rem;
		border: 1px solid #334155;
	}

	.badge {
		display: inline-block;
		padding: 0.2rem 0.6rem;
		border-radius: 1rem;
		font-size: 0.8rem;
		text-transform: uppercase;
	}

	.badge.pending { background: #ca8a04; }
	
	.error { color: #f87171; }
</style>
