function handleResponse(response) {
	return response.text().then(text => {
	  let data;
	  try {
		data = text ? JSON.parse(text) : {};
	  } catch (e) {
		data = { message: 'An error occurred while processing the response.' };
	  }
  
	  if (!response.ok) {
		const { user, logout } = useAuthStore();
		if ([401, 403].includes(response.status) && user) {
		  logout();
		}
  
		const error = (data && data.message) || response.statusText;
		return Promise.reject(error);
	  }
  
	  return data;
	});
  }
  