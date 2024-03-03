const TaskCard = ({ taskName, taskDescription, deadlineTime, onDelete }) => {
  return (
    <div className="max-w-[300px] w-full flex-shrink-0">
      <div className="flex justify-between">
        <span className="font-bold text-lg">{taskName}</span>
        <div className="flex gap-1">
        <button onClick={onDelete}>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            strokeWidth={1.5}
            stroke="currentColor"
            className="w-8 h-8"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              d="m9.75 9.75 4.5 4.5m0-4.5-4.5 4.5M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"
            />
          </svg>

          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            strokeWidth={1.5}
            stroke="currentColor"
            className="w-8 h-8"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              d="M9 12.75 11.25 15 15 9.75M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"
            />
          </svg>
          </button>
        </div>
      </div>
      <p>{taskDescription}</p>
      <span className="text-[#7e7e7e]">
        {new Date(deadlineTime).toLocaleString("default", {
          month: "long",
          day: "numeric",
          year: "numeric",
          hour: "numeric",
          minute: "numeric",
          hourCycle: "h12",
        })}
      </span>
    </div>
  );
};

function FriendTask({ tasks }) {
  const handleDelete = (index) => {
    // Create a new array without the task at the specified index
    const updatedTasks = [...tasks.slice(0, index), ...tasks.slice(index + 1)];
    setTasks(updatedTasks);
  };
  return (
    <div className="h-full flex flex-col max-w-full">
      <span className="text-2xl font-bold">Friend Tasks</span>
      <div className="flex-1 border-2 rounded-lg p-5 gap-5 overflow-x-scroll flex w-full max-w-full">
        {tasks &&
          tasks.map((task, _i) => {
            return <TaskCard key={_i} {...task} onDelete={() => handleDelete(_i)}/>;
          })}
      </div>
    </div>
  );
}

export default FriendTask;
