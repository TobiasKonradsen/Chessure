

import React from 'react';
import './CanvasBlock.css';

import Piece from '../Piece/Piece';


class CanvasBlock extends React.Component {
    constructor(props){
      super(props)
      // this.defineColor = this.defineColor.bind(this)
      this.dragOver = this.dragOver.bind(this)
      this.onDropHandler = this.onDropHandler.bind(this)
      this.handleDragOver = this.handleDragOver.bind(this)
    }
    renderPiece(){
      if (this.props.type){
        return <Piece chessIndex={this.props.chessIndex} team={this.props.team}
          possibleMoves={this.props.possibleMoves}
          type={this.props.type}
          showMoves={this.props.showMoves}
          redrawBackground={this.props.redrawBackground}/>
      }
    }


    dragOver(e) {
      e.preventDefault();
    }

    onDropHandler(e){
      
      e.preventDefault();
      var jsonData = e.dataTransfer.getData("pieceInfo");
      var data = JSON.parse(jsonData)
      // console.log(data)
      if (data.possibleMoves.includes(this.props.chessIndex)){
            const prevPiece = document.getElementById(data.target_id)
            console.log(prevPiece)
            e.target.replaceChildren(prevPiece);
            // Need some serverbased response for the move here :)
      }

    }

    handleDragOver(e){
      e.preventDefault();
    }

    

    render(){
      return (
        <div className="CanvasBlock" 
        style={{backgroundColor: this.props.color}}
        onDrop={this.onDropHandler}
        onDragOver={this.handleDragOver}
        onDragEnter= {this.handleDragEnter}>
          {this.renderPiece()}
          
        </div>
      )
    };
  }
export default CanvasBlock