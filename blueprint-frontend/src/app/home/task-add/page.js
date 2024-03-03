import TaskForm from "../../../components/AppHome/TaskAdd/taskForm"

export default function TaskAdd() {
    return (
        <div className="flex flex-row min-h-screen justify-center items-center w-full">
            <div className="w-fit">
                <TaskForm />
            </div>
        </div>
    );
}