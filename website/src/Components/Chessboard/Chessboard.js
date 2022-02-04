

import React from 'react';


import './Chessboard.css';

import Canvas from '../Canvas/Canvas';

class Chessboard extends React.Component {
    constructor(props){
      super(props)
    }
  
    render(){
      return (<div className='Chessboard'>
        <Canvas sideLength = {8} boardState={this.props.boardState}/>
        </div>
        )
    };
  }


  export default Chessboard