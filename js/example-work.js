import React from 'react';

class ExampleWork extends React.Component {
  render() {
    return (
      <section className="section section--alignCentered section--description">
      { this.props.work.map( (example,idx) => {
        return (
          <ExampleWorkBubble />
        )
      })}



      </section>


    )
  }
}

class ExampleWorkBubble extends React.Component {
  render() {
    return (
      <div className="section__exampleWrapper">
        <div className="section__example">
          <img alt="example screenshot of a project involving code"
             className="section__exampleImage"
             src="images/example1.png"/>
          <dl className="color--cloud">
            <dt className="section__exampleTitle section__text--centered">
               Work ExampleWork
            </dt>
            <dd></dd>
          </dl>
        </div>
      </div>
    )
  }
}


export default ExampleWork
