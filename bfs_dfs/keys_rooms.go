// LEETCODE@ 841. Keys and Rooms
//
// --END--


package bfs_dfs


func canVisitAllRooms(rooms [][]int) bool {
	vst := make(map[int]bool)

	dfs(&vst, &rooms, 0)
	return len(vst) == len(rooms)
}

func dfs(vst *map[int]bool, rooms *[][]int, roomID int) {
	(*vst)[roomID] = true

	for _, nxtRoomID := range (*rooms)[roomID] {
		if _, ok := (*vst)[nxtRoomID]; !ok {
			dfs(vst, rooms, nxtRoomID)
		}
	}
}