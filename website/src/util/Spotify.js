import clientIdObj from './clientapi'
const clientId = clientIdObj.clientId
const redirectUri = 'https://aware-coat.surge.sh/'
let accessToken;
const Spotify = {
    getAccessToken(){
        if (accessToken){
            return accessToken
        }
        const accessTokenMatch = window.location.href.match(/access_token=([^&]*)/)
        const expiresInMatch = window.location.href.match(/expires_in=([^&]*)/)

        if (accessTokenMatch && expiresInMatch){
            accessToken = accessTokenMatch[1]
            const expiresIn = Number(expiresInMatch[1])
            window.setTimeout(() => accessToken = '', expiresIn * 1000);
            window.history.pushState('Access Token', null, '/');
            return accessToken
        } 
        const accessUrl = `https://accounts.spotify.com/authorize?client_id=${clientId}&response_type=token&scope=playlist-modify-public&redirect_uri=${redirectUri}`
        window.location = accessUrl
    
        
    },

    search(term){
        const accessToken = Spotify.getAccessToken()
        const endpointSearch = `https://api.spotify.com/v1/search?type=track&q=${term}`
        return fetch(endpointSearch, {headers: {Authorization: `Bearer ${accessToken}` }}).then((response) =>{
            if (response.ok){
                return response.json()
            } else{
                console.log(response)
            }
            }
        ).then(jsonResponse => {
            if (!jsonResponse.tracks) {
                return []
            }

            return jsonResponse.tracks.items.map(track => {
                        return {id: track.id,
                        name: track.name,
                        artist: track.artists[0].name,
                        album: track.album.name,
                        uri: track.uri
                        }}
            
                    )
            } 
            )
    },
    savePlaylist(playlistName, trackURIs){
        if (!playlistName || !trackURIs.length){
            return
        }
        const accessToken = Spotify.getAccessToken()
        const headers = {Authorization: `Bearer ${accessToken}` }
        let userId;
        // Fetch the username of the user.
        return fetch('https://api.spotify.com/v1/me', {headers: headers}).then((response) =>{
            return response.json()
            }
        ).then((jsonResponse)=>{
            console.log(jsonResponse)
            userId = jsonResponse.id
            
            return fetch(`https://api.spotify.com/v1/users/${userId}/playlists`, 
                    {
                        headers: headers,
                        method: 'POST',
                        body: JSON.stringify({name: playlistName}),
                    }).then(response => {
                        return response.json()}
                    ).then(jsonResponse => {
                        const playlistId = jsonResponse.id
                        return fetch(`https://api.spotify.com/v1/users/${userId}/playlists/${playlistId}/tracks`,
                        {headers: headers,
                        method: 'POST',
                        body: JSON.stringify({uris: trackURIs}),
                        })
                    })
        })

        

    }
}

export default Spotify