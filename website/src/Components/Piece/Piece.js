
import React from 'react';
import './Piece.css';

import whiteQueen from './graphics/Chess_qlt60.png';
import whiteKing from './graphics/Chess_klt60.png';
import whiteKnight from './graphics/Chess_nlt60.png';
import whiteRook from './graphics/Chess_rlt60.png';
import whitePawn from './graphics/Chess_plt60.png';
import whiteBishop from './graphics/Chess_blt60.png';


import blackQueen from './graphics/Chess_qdt60.png';
import blackKing from './graphics/Chess_kdt60.png';
import blackKnight from './graphics/Chess_ndt60.png';
import blackRook from './graphics/Chess_rdt60.png';
import blackPawn from './graphics/Chess_pdt60.png';
import blackBishop from './graphics/Chess_bdt60.png';



class Piece extends React.Component {
    constructor(props){
        super(props)
        // this.addTrack = this.addTrack.bind(this)
        // this.removeTrack = this.removeTrack.bind(this)
        this.showPossibleMoves = this.showPossibleMoves.bind(this)
        this.redrawBackground = this.redrawBackground.bind(this)
        this.dragStart = this.dragStart.bind(this)
    }

    renderGraphics(){
      // This is freaking stupid code
      let source = ''
      let alt = ''
      if (this.props.team === 'White'){
        if (this.props.type === 'Queen'){
          source = whiteQueen
          alt = 'White queen'
        }
        if (this.props.type === 'King'){
          source = whiteKing
          alt = 'White king'
        }
        if (this.props.type === 'Knight'){
          source = whiteKnight
          alt = 'White Knight'
        }
        if (this.props.type === 'Bishop'){
          source = whiteKnight
          alt = 'White Bishop'
        }
        if (this.props.type === 'Rook'){
          source = whiteRook
          alt = 'White Rook'
        }
        if (this.props.type === 'Pawn'){
          source = whitePawn
          alt = 'White Pawn'
        }
        
      }
      
      if (this.props.team === 'Black'){
        if (this.props.type === 'Queen'){
          source = blackQueen
          alt = 'Black queen'
        }
        if (this.props.type === 'King'){
          source = blackKing
          alt = 'Black King'
        }
        if (this.props.type === 'Knight'){
          source = blackKnight
          alt = 'Black Knight'
        }
        if (this.props.type === 'Bishop'){
          source = blackBishop
          alt = 'Black Bishop'
        }
        if (this.props.type === 'Rook'){
          source = blackRook
          alt = 'Black Rook'
        }
        if (this.props.type === 'Pawn'){
          source = blackPawn
          alt = 'Black Pawn'

        }
        
      }
      if (source){
        return <img id={this.props.chessIndex+100} src={source} alt ={alt} style={{zIndex:10}}
         onMouseDown={this.showPossibleMoves}
         onMouseUp={this.redrawBackground}
         onDragEnd={this.redrawBackground}
         onDragStart={this.dragStart}
         draggable='true'/>
      }


    }

    dragStart(e) {
      console.log(this.props.id)
      var data = JSON.stringify({target_id: e.target.id, own_id:this.props.chessIndex+100, possibleMoves: this.props.possibleMoves})
      e.dataTransfer.setData("pieceInfo", data);
    }

    redrawBackground(){
      this.props.redrawBackground()
    }
    showPossibleMoves(){
      this.props.showMoves(this.props.possibleMoves)
    }

    render(){
      return (
        <div className="Piece">
          {this.renderGraphics()}  
        </div>

      )
    };
  }

export default Piece;
