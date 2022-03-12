//add a new job to track 
function AddJobForm() {
    return (
        <div>
        <form className='newjob-form'>
        <input type='text' placeholder='Company Name' className='companyname-input'></input>
        <input type='text' placeholder='Job Title' className='jobtitle-input'></input>
        <input type='text' placeholder='Job Description' className='jobdescription-input'></input>
        <input type='date' placeholder='Date Applied' className='date-input'></input>
        <input type='url' placeholder='Company Website' className='companyurl-input'></input>
        <input type='text' placeholder='Notes' className='notes-input'></input>
        <button className='submit'>Add Job</button>
        </form>
        </div>
    )
}


//app function 
function App() {
    return (
        <div className='job-app'>
            <h1>Job Search Tracker</h1>
            <AddJobForm />
        </div>
    );
}

ReactDOM.render(<App />, document.querySelector('#root'));