

import React from 'react';

import CanvasBlock from '../CanvasBlock/CanvasBlock';
import './Canvas.css';




class Canvas extends React.Component {
    constructor(props){
      super(props)
      this.state = {
        colors:Array.apply(0, Array(this.props.sideLength**2)).map((x,i) => {
          return {id: i, color:this.defineColor(i)}
        })
      }
      
      this.showMoves = this.showMoves.bind(this)
      this.redrawBackground = this.redrawBackground.bind(this)

    }
    
    defineColor(index){
      // Set the color of the div canvasblocks.
      const offset = Math.floor(index / 8)
      if ((offset+index) % 2 === 0){
         return 'grey'
      }
      else {
        return 'white'
      }
      
    }
    redrawBackground(){
      this.setState({
        colors: Array.apply(0, Array(this.props.sideLength**2)).map((x,i) => {
        return {id: i, color:this.defineColor(i)}
        })
      })
    }
    showMoves(moves){
      this.setState({
        colors: this.state.colors.map((el) => {
            if (moves.includes(el.id)){
              return {color:'green', id: el.id}
            } else {
              return el
            } 
          })
        })
    }


    createCanvas(){
        return Array.apply(0, Array(this.props.sideLength**2)).map((x, i) => {
            // this.defineColor(i)
            for (var k=0; k < this.props.boardState.length; k++) {
              let piece = this.props.boardState[k]
               if (piece.position === i){
                 return < CanvasBlock  key={i} chessIndex={piece.position}
                  team={piece.team} possibleMoves={piece.possibleMoves} type={piece.type}
                  color={this.state.colors[i].color} showMoves={this.showMoves} redrawBackground={this.redrawBackground}/>
               }
            } 
            return <CanvasBlock key={i} chessIndex={i} team='' possibleMoves='' type='' color={this.state.colors[i].color} />;
          })
    }

    render(){
      return (
        <div className='ChessCanvas'>
          {this.createCanvas()}
        </div>
       
        )
    };
  }


  export default Canvas