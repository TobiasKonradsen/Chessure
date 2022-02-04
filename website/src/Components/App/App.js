// import logo from './logo.svg';
import React from 'react';
import './App.css';



import Chessboard from '../Chessboard/Chessboard';

// import SearchBar from '../SearchBar/SearchBar';
// import SearchResults from '../SearchResults/SearchResults';
// import Playlist from '../Playlist/Playlist';
// import Spotify from '../../util/Spotify';


class App extends React.Component {
  constructor(props){
    super(props)
    this.state = {
      // Position from 1 to sidelength*2
      boardState: [
        {type:'Queen', team:'White', position:0, possibleMoves:[1,2,3,4,5,6,7,8,9,10,11,12,13]},
        {type:'Queen', team:'White', position:1, possibleMoves:[1,2,3,4,5,6,7,8,9,10,11,12,13]},
        {type:'Queen', team:'White', position:2, possibleMoves:[1,2,3,4,5,6,7,8,9,10,11,12,13]},
        {type:'King', team:'Black', position:3, possibleMoves:[1,2,3,4,5,6,7,8,9,10,11,12,13]},
        {type:'Pawn', team:'Black', position:4, possibleMoves:[1,2,3,4,5,6,7,8,9,10,11,12,13]},
      ], 
                  }
    // this.addTrack = this.addTrack.bind(this)
    // this.removeTrack = this.removeTrack.bind(this)
    // this.updatePlaylistName = this.updatePlaylistName.bind(this)
    // this.savePlaylist = this.savePlaylist.bind(this)
    // this.search = this.search.bind(this)
  }
  
  render(){
    return (
    <div>
      <h1>Che<span className="highlight">ss</span>ure</h1>
      <div className="App">
          <Chessboard boardState={this.state.boardState}/>
      </div>
    </div>
    )
  };
}



export default App;
