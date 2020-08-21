PROJ_BASE="$(dirname "${BASH_SOURCE[0]}")"
CD=$(pwd)
cd "$PROJ_BASE" || exit
PROJ_BASE=$(pwd)
export PROJ_BASE
cd "$CD" || exit

function dkdb {
  docker run --name mentira -e POSTGRES_USER=mentira -e POSTGRES_PASSWORD=mentira \
    -p 5432:5432 \
    -v "$PROJ_BASE"/dkdata/postgres-mentira:/var/lib/postgresql/data \
    postgres:12
}