function TaskForm() {

    function submitForm(formData) {
        {/** yes. */}
    }

    return (
        <div className="h-full flex flex-col max-w-full">
            <span className="text-2xl font-bold">Task Add</span>
            <div className="flex-1 border-2 rounded-lg p-5 gap-5 max-w-full">
                <form className="flex flex-col gap-5 items-center">
                    <div className="flex flex-col min-w-[300px]">
                        <label className="text-lg font-bold">Recipient</label>
                        <input className="border-2 rounded-lg" type="text" name="recieverID"/>
                    </div>
                    <div className="flex flex-col min-w-[300px]">
                        <label className="text-lg font-bold" >Task Name</label>
                        <input className="border-2 rounded-lg" type="text" name="taskName"/>
                    </div>
                    <div className="flex flex-col min-w-[300px]">
                        <label className="text-lg font-bold">Task Description</label>
                        <input className="border-2 rounded-lg min-h-[120px]" type="text" name="taskDescription"/>
                    </div>
                    <div className="flex flex-col min-w-[300px]">
                        <label className="text-lg font-bold">End Date</label>
                        <input className="border-2 rounded-lg" type="text" name="deadlineTime"/>
                    </div>
                    <div className="flex flex-col min-w-[300px]">
                        <label className="text-lg font-bold">Duration</label>
                        <input className="border-2 rounded-lg" type="text" name="duration"/>
                    </div>
                    <button type="submit" className="border-2 rounded-xl ml-0 min-w-[120px]">Send</button>
                </form>
            </div>
        </div>
    );
}

export default TaskForm